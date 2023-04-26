from pyngrok import ngrok

# Criar um túnel HTTP na porta 8000
public_url = ngrok.connect(8000, "http")

print("Túnel criado! URL pública: ", public_url)
