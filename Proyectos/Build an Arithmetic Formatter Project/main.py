def arithmetic_arranger(problems, show_answers=False):
    linea1=[]
    linea2=[]
    linea3=[]
    linea4=[]
    final_result=''

    for problem in problems:
        num1, operator, num2 = problem.split()
        width=max(len(num1), len(num2)) + 2
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        elif not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        elif len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        elif len(problems) > 5:
            return "Error: Too many problems."

        else:
            if operator == '+':
                result = str(int(num1)+int(num2))
            else:
                result = str(int(num1)-int(num2))
        
        linea1.append(num1.rjust(width))
        linea2.append(operator + num2.rjust(width - 1))
        linea3.append('-'*width)

        final_result='    '.join(linea1)+'\n' + \
                     '    '.join(linea2)+'\n' + \
                     '    '.join(linea3)
        
        if show_answers:
            linea4.append(result.rjust(width))
            final_result += '\n'+'    '.join(linea4)

    return final_result


arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])