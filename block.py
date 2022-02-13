
import json
import os
import hashlib

BLOCKCHAIN_DIR = 'blockchain/'

def get_hash(prev_block):
    with open(BLOCKCHAIN_DIR + prev_block, 'rb') as f:
        content = f.read()
    return hashlib.md5(content).hexdigest()

def check_integrity():
    files = sorted(os.listdir(BLOCKCHAIN_DIR), key=lambda x: int(x))
    
    results = []
    
    for file in files[1:]:
        with open(BLOCKCHAIN_DIR + file) as f:
            block = json.load(f)
        
        prev_hash = block.get('prev_block').get('hash')
        prev_filename = block.get('prev_block').get('filename')
        
        actual_hash = get_hash(prev_filename)
        if prev_hash == actual_hash:
            res = 'OK'
        else:
            res = 'Was Changed'

        print(f'Block {prev_filename} : {res}')
        results.append({'block' : prev_filename, 'results' : res})
    return results
def write_block(Team1, Team2, Time):

    blocks_count = len(os.listdir(BLOCKCHAIN_DIR))
    prev_block = str(blocks_count)
    

    data = {
        "Team1": Team1,
        "Team2": Team2,
        "Time": Time,
        "prev_block": {
            "hash": get_hash(prev_block),
            "filename": prev_block
        }
    }

    current_block = BLOCKCHAIN_DIR + str(len(os.listdir(BLOCKCHAIN_DIR))+1)

    with open(current_block, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.write('\n')


def main():
    write_block(Team1="PSG.LSD", Team2="Nigma", Time="5/05/2022-13:00")
    write_block(Team1="PSG.LSD", Team2="OG", Time="5/05/2022-13:00")
    write_block(Team1="OG", Team2="Nigma", Time="5/05/2022-13:00")
    write_block(Team1="PSG.LSD", Team2="T1", Time="5/05/2022-13:00")
    write_block(Team1="T1", Team2="FNATIC", Time="5/05/2022-13:00")
    write_block(Team1="PSG.LSD", Team2="FNATIC", Time="5/05/2022-13:00")
    write_block(Team1="T1", Team2="PSG.LGD", Time="5/05/2022-13:00")
    write_block(Team1="BOOM", Team2="Nigma", Time="5/05/2022-13:00")
    write_block(Team1="T1", Team2="BOOM", Time="5/05/2022-13:00")
    write_block(Team1="FNATIC", Team2="BOOM", Time="5/05/2022-13:00")
    check_integrity()

if __name__ == '__main__':
    main()
