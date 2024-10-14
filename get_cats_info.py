def get_cats_info(path):
    cats = [] 
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')

                cat = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                cats.append(cat)
        return cats

    except:
        print("File not found or corrupted.")
        return []
   
