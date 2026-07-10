from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.deepseek import DeepSeek
from email.message import EmailMessage
from dotenv import load_dotenv

from datetime import datetime
import os, smtplib, time

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
DESTINATARIOS = os.getenv("DESTINATARIOS", "")
hora_envio = os.getenv("SENT_AT", "")

def envia_email(assunto, conteudo, destinatarios):
    """Envia um email com o assunto e conteúdo fornecidos."""
    try:
        msg=EmailMessage()
        msg['Subject'] = assunto
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = DESTINATARIOS

        msg.set_content(conteudo, charset='utf-8')

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        print(f"Email enviado com sucesso para: {destinatarios}")
        return True

    except Exception as e:
        print(f"Erro ao enviar email para {destinatarios}: {e}")
        return False


agente = Agent(
    model=DeepSeek(id="deepseek-v4-flash"),
    tools=[TavilyTools()],
    debug_mode=False
)

if __name__ == "__main__":
    from prompt2 import prompt_pro_agente

    print(f"Iniciando o processo de geração da newsletter às {hora_envio}")
    ultimo_envio = None

    while True:
        agora = datetime.now()

        if agora.strftime("%H:%M") == hora_envio and ultimo_envio != agora.date():
            print("Gerando newsletter com o Agente...")

            try:
                # 1. O agente pesquisa e CRIA o conteúdo da newsletter (ele retorna um objeto RunResponse)
                prompt_data = f"DATA: {agora.strftime('%d/%m/%Y')}\n\n{prompt_pro_agente}"
                resposta_agente = agente.run(prompt_data)

                # Extrai o texto gerado pelo agente
                conteudo_newsletter = resposta_agente.content

                # 2. O Python assume o controle do envio baseado na sua lista de destinatários
                lista_destinatarios = [email.strip() for email in DESTINATARIOS.split(",") if email.strip()]
                assunto_email = f"Sua Newsletter Diária - {agora.strftime('%d/%m/%Y')}"


                for email_atual in lista_destinatarios:
                    print(f"Envianto para: {email_atual}")
                    envia_email(assunto_email, conteudo_newsletter, email_atual)
                    time.sleep(2) # delay de segurança entre envios

                ultimo_envio = agora.date()
                print("Newsletter gerada e enviada para TODOS com sucesso!!!!!")

                print("Encerrando o programa após o envio.")
                break

            except Exception as e:
                print(f"Erro ao gerar ou enviar a newsletter: {e}")
                time.sleep(10)  # Aguarda 1 minuto antes de tentar novamente
        
        else:
            time.sleep(10)  # Aguarda 10 segundos antes de verificar novamente
