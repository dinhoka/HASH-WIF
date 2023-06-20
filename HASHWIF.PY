from pycoin.key import Key

def get_address_from_private_key(private_key_wif):
    try:
        # Cria uma instância da chave privada a partir do formato WIF
        private_key = Key.from_text(private_key_wif)

        # Obter o endereço Bitcoin correspondente à chave privada
        address = private_key.address()

        return address
    except Exception as e:
        print("Erro ao obter endereço:", str(e))
        return None

# Chave privada no formato Wallet 
        
 import Format (WIF)
private_key_wif = ""

# Obter o endereço correspondente à chave privada
address = get_address_from_private_key(private_key_wif)

if address:
    print("Endereço da carteira:", address)
