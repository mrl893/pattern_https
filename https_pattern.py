NOT_FOUND = 404
retcode = 200

match retcode:
    case not_found:
        print("not found")
print(f"Current value of{NOT_FOUND}")


