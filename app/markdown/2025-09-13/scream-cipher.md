# SCREAM CIPHER (“ǠĂȦẶAẦ ĂǍÄẴẶȦ”)

You've probably heard of [stream ciphers](https://en.wikipedia.org/wiki/Stream_cipher), but what about a *scream cipher* 😱?
Today I learned there are more “[Latin capital letter A](https://utf8.xyz/latin-capital-letter-a-)”
Unicode characters than there are letters in the English alphabet. You know what that means, it's time to scream:

<!-- more -->

```python
CIPHER = {
"A":"A",  # Round-trip!
"B":"Á","G":"Ẳ","L":"Ậ","Q":"Ǟ","V":"À",
"C":"Ă","H":"Ẵ","M":"Ầ","R":"Ȧ","W":"Ả",
"D":"Ắ","I":"Ǎ","N":"Ẩ","S":"Ǡ","X":"Ȃ",
"E":"Ặ","J":"Â","O":"Ẫ","T":"Ạ","Y":"Ā",
"F":"Ằ","K":"Ấ","P":"Ä","U":"Ȁ","Z":"Ą",
}
CIPHER.update({map(str.lower, kv) for kv in CIPHER.items()})
UNCIPHER = {v: k for k, v in CIPHER.items()}

def SCREAM(text: str) -> str:
    return "".join(CIPHER.get(ch, ch) for ch in text)

def unscream(scream: str) -> str:
    return "".join(UNCIPHER.get(ch, ch) for ch in scream)


print(s := SCREAM("SCREAM CIPHER"))
# ǠĂȦẶAẦ ĂǍÄẴẶȦ

print(unscream(s))
# SCREAM CIPHER
```
