import cherrypy
import transformers
from transformers import GPT2Tokenizer, TFGPT2LMHeadModel

class SayWords:
    @cherrypy.expose
    def index(self, words=None):

        def do_tokenization_from_gpt2(words_list):

            tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
            model = TFGPT2LMHeadModel.from_pretrained("gpt2") # remove pad_token_id=tokenizer.eos_token_id

            prompt = " ".join(words_list)
            print("prompt type",type(prompt))
            input_ids = tokenizer.encode(prompt, return_tensors="tf")
            print("input_ids: ", input_ids)

            # generate up to 30 tokens
            beam_output = model.generate(
                input_ids, 
                max_length=50,
                num_beams=5, 
                no_repeat_ngram_size=4, 
                early_stopping=True
            )

            print("beam_output",beam_output)
            print("beam_output",type(beam_output))

            sentence_return = tokenizer.decode(beam_output[0])
            print("type sentence_return: ",type(sentence_return))
            print("sentence_return: ",sentence_return)
            
            return sentence_return

        if words:
            words_list = words.split('%')
            sentence_return = do_tokenization_from_gpt2(words_list)
            returnstring = f"""
            <html><body>
            Your input: {words}
            <hr>
            Your answer: 
            {sentence_return}
            <hr>
            </body></html>
            """
            return returnstring
        else:
            return '<html><body>Please enter `words` in the URL as a query parameter, seperated by `%` for example: `/?words=how%are%you?` </body></html>'
    


if __name__ == '__main__':
    cherrypy.quickstart(SayWords(), '/', {'global': {'server.socket_host':'0.0.0.0','server.socket_port': 8080}})