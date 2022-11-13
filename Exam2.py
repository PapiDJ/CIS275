from ArrayStack import ArrayStack

def main():
    current_value = 0
    s = ArrayStack()
    o = ArrayStack()
    while True:
        print(f'Current value: {current_value}')
        ui = input("Enter a number, 'u' to undo, 'r' to redo, or 'q' to quit: ")
        if ui == 'u':
            if s.is_empty():
                print("Nothing to undo")
            else:
                o.push(current_value)
                current_value = s.pop()
        elif ui == 'r':
            if o.is_empty():
                print("Nothing to redo")
            else:
                s.push(current_value)
                current_value = o.pop()
        elif ui == 'q':
            break
        elif ui.isdigit():
            op = input("Enter an operator (+, -, *, /): ")
            o.clear()
            result = eval(f'{current_value} {op} {ui}')
            s.push(current_value)
            print(f'{current_value} {op} {ui} = {result}')
            current_value = result
        else:
            raise ValueError("Invalid input")
            
main()

