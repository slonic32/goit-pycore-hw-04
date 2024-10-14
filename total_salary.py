def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0 
            count = 0 

            for line in file:
                name, salary = line.strip().split(',')

                total += int(salary)
                count += 1

        if count:
            average = total / count

        return total, average

    except:
        print("File not found or corrupted.")
        return 0, 0
   
