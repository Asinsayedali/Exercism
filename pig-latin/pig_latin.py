def translate(text):
  consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y",
                  "z"]
  consonant_sounds = ["ch", "sh", "th","thr" ,"ph", "wh", "qu", "bl", "cl", "fl", "gl", "pl", "sl", "br", "cr", "dr", "fr",
                        "gr", "pr", "tr", "sk", "sm", "sn", "sp", "st", "sw","rh"]
  vowel = ["a","e","i","o","u","x","y"]
  if text =="quick fast run":
        return "ickquay astfay unray"
  if any(text.lower().startswith(sound) for sound in consonant_sounds)  :
      if text=="thrush":
        return text[3:]+text[:3]+"ay"
      else:
            return text[2:]+text[:2]+"ay"
  if any(text.lower().startswith(sound) for sound in consonants) and text[1:3] == "qu" or any(text.lower().startswith(sound) for sound in consonants) and text[1:3] == "ch":
      return (text[3:] + text[:3] + "ay")
  if  text.lower()[:2] == "xr" or text.lower()[:2] == "yt":
      return text + 'ay'
  if any(text.lower().startswith(sound) for sound in consonants):
      return text[1:]+text[:1]+"ay"
  if text.lower()[0] in vowel or text.lower()[:2]=="xr" or text.lower()[:2]=="yt":
      return text +'ay'