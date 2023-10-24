def  http_error(status):
    match status:
        case "401":
            return "Unauthorized"
        case "401": 
            return "Bad request"
        case "403":
              return "Forbidden"
        case 404:
              return "Not found"
        case 418:
              return "I'm a teapot"
        case _:
              return "Something else"
