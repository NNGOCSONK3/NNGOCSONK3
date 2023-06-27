import os

def make_commit(days: int):
    if days >5:
        # push
        return os.system("git push")
    else:
        dates = f'{days} days ago'

        with open('text.txt', 'a') as file:
            file.write(f'{dates}\n')
        # staging
        os.system('git add text.txt')
        #  commit
        os.system('git commit --date="'+dates+'" -m "Fist commit"') 
        return days * make_commit(days-1)                                                
make_commit(365)