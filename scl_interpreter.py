from token_types import *




#Function for categorizing tokens
def token_catorizer(token):
    if token in token_list["keywords"]:
        return {"type": "Keyword", "id": token_list["keywords"][str(token)], "value": token}
    elif token in token_list["operators"]:
        return {"type": "Operator", "id": token_list["operators"][str(token)], "value": token}
    # TODO: Figure out how I want to make this work
    elif token in token_list["special symbols"]:
        if token == "'":
            return 
        if token == '"':
            return 