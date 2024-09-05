import os
from dotenv import load_dotenv
import deepl

load_dotenv()
DEEPL_API_KEY=os.environ["DEEPL_API_KEY"]

translator = deepl.Translator(DEEPL_API_KEY)

# result_ja = translator.translate_text("How can I translate it into Japanese?", target_lang="JA")
# print(result.detected_source_lang)
# print(result.text)
# print(result.__dict__)
# print(result_ja.text)

def translateText(text):
  # text = "日本語へ訳すにはどうしたらいい？"
  result = translator.translate_text(text, target_lang="EN-US")
  if result.detected_source_lang != "JA":
    result = translator.translate_text(text, target_lang="JA")
  return result