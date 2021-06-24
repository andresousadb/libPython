import pytest

from libpython_01.spam.enviador_de_email import EmailInvalido
from libpython_01.spam.enviador_de_email import Enviador

def test_criar_enviar_email():
    enviador = Enviador ()
    assert enviador is not None

@pytest.mark.parametrize(
    'remetente',
    ['andresousadb@gmail.com','andre.ferreira@viagensmontreal.com']
)
def test_rementente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'sousa705@gmail.com',
        'Testando',
        'bora ver esse envio'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['','andre']
)
def test_rementente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'sousa705@gmail.com',
            'Testando',
            'bora ver esse envio'
        )



