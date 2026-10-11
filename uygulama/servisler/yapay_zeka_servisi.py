def yanit_uret(self, kullanici_mesaji, sohbet_gecmisi=None):
saglayici = current_app.config.get('AI_PROVIDER', 'groq').lower()
if saglayici == 'openai':
return self._openai_cagir(...) # OpenAI kullan
elif saglayici == 'groq':
return self._groq_cagir(...) # Groq kullan (varsayılan)
else:
return self._gemini_cagir(...) # Gemini kullan