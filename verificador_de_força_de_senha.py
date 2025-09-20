"""
Verificador de força da senha que classifica as senhas em 'Forte' , 'Média' e 'Fraca'

Este módulo contém a função `check_password_strength()` que analisa uma string 
de senha com base em critérios de segurança e retorna o seu nível de força.

Regras de Classificação:
"Forte": - Atende a todos os 5 requisitos.
"Média": - Atende ao requisito de comprimento e a mais 2 outros.
"Fraca": - Qualquer outra combinação.

Critérios de verificação:
1. Mínimo de 8 caracteres.
2. Pelo menos uma letra minúscula de (a - z).
3. Pelo menos uma letra maiúscula de (A - Z).
4. Pelo menos um número de (0-9).
5. Pelo menos um caractere especial (ex: @,#,!,-)

Uso:
    Execute este script a partir da linha de comando e digite uma senha
    quando solicitado. O programa imprimirá a força da senha.
"""
import string

def check_password_strength(password: str):
    size = len(password)
    
    have_eight_characters = True if size >= 8 else False
    has_one_lowercaser_letter = any(letter.islower() for letter in password)
    has_one_capital_letter = any(letter.isupper() for letter in password)
    have_numbers_of_zero_a_nine = any(caractere.isdigit() for caractere in password)
    has_special_characters = any(caractere in string.punctuation for caractere in password)
    
    requirements = [have_eight_characters, has_one_capital_letter , 
    has_one_lowercaser_letter , have_numbers_of_zero_a_nine ,
    has_special_characters]

    numbers_of_true_conditions = sum(requirements)

    if numbers_of_true_conditions == 5:
        return "Senha Forte"
    elif have_eight_characters and numbers_of_true_conditions >= 3:
        return "Senha Média"
    else:
        return "Senha Fraca"

if __name__ == "__main__":
    user_input = input("Digite sua senha para verificação: : ") 
    result = check_password_strength(user_input)
    print(result)