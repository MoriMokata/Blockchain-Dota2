
import json
import os
import hashlib

BLOCKCHAIN_DIR = 'blockchain/'

def Create_hash(prev_block):
    with open(BLOCKCHAIN_DIR + prev_block) as f:
        block = json.load(f)
    
    prev_hash = block.get('prev_block').get('hash')
    prev_filename = block.get('prev_block').get('filename')
    Team1 = block.get('Team1')
    Team2 = block.get('Team2')
    Time =  block.get('Time')
    data = (f"Team1 : {Team1} Team2 : {Team2} Time : {Time} \n Previous hash : {prev_hash} filename : {prev_filename}")
    return hashlib.sha256(data.encode()).hexdigest()

def Check_hash(prev_block,prev_hash):
    with open(BLOCKCHAIN_DIR + prev_block) as f:
        block = json.load(f)
    prev_hash1 = block.get('prev_block').get('hash')
    prev_filename = block.get('prev_block').get('filename')
    Team1 = block.get('Team1')
    Team2 = block.get('Team2')
    Time =  block.get('Time')
    data = (f"Team1 : {Team1} Team2 : {Team2} Time : {Time} \n Previous hash : {prev_hash} filename : {prev_filename}")
    return hashlib.sha256(data.encode()).hexdigest()

def check_integrity():
    files = sorted(os.listdir(BLOCKCHAIN_DIR), key=lambda x: int(x))
    
    results = []
    index = 0
    prev_hash = []
    prev_hash.append("Genisis Block")
    for file in files[1:]:
        with open(BLOCKCHAIN_DIR + file) as f:
            block = json.load(f)
        
        prev_hash_db = block.get('prev_block').get('hash')
        prev_filename = block.get('prev_block').get('filename')
        hash = Check_hash(prev_filename,prev_hash[index])
        prev_hash.append(hash)

        if prev_hash_db == prev_hash[index+1]:
            res = 'OK'
        else:
            res = 'Was Changed'

        print("Pre",prev_hash_db)
        print("Actual",prev_hash[index+1])
        print(f'Block {prev_filename} : {res}')
        results.append({'block' : prev_filename, 'results' : res})
        index = index+1
    return results

def show_data():
    files = sorted(os.listdir(BLOCKCHAIN_DIR), key=lambda x: int(x))
    data = []
    for file in files[1:]:
        with open(BLOCKCHAIN_DIR + file) as f:
            block = json.load(f)
        
        prev_filename = block.get('prev_block').get('filename')
        Team1 = block.get('Team1')
        Team2 = block.get('Team2')
        Time =  block.get('Time')
        

        data.append({'block' : prev_filename, 'Team1' : Team1, 'Team2' : Team2, 'Time' : Time})
    return data


def write_block(Team1, Team2, Time):

    blocks_count = len(os.listdir(BLOCKCHAIN_DIR))
    prev_block = str(blocks_count)
    

    data = {
        "Team1": Team1,
        "Team2": Team2,
        "Time": Time,
        "prev_block": {
            "hash": Create_hash(prev_block),
            "filename": prev_block
        }
    }

    current_block = BLOCKCHAIN_DIR + str(len(os.listdir(BLOCKCHAIN_DIR))+1)

    with open(current_block, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.write('\n')


def main():
    # write_block(Team1="PSG.LSD", Team2="Nigma", Time="5/05/2022-13:00")
    # write_block(Team1="PSG.LSD", Team2="OG", Time="5/05/2022-13:00")
    # write_block(Team1="OG", Team2="Nigma", Time="5/05/2022-13:00")
    # write_block(Team1="PSG.LSD", Team2="T1", Time="5/05/2022-13:00")
    # write_block(Team1="T1", Team2="FNATIC", Time="5/05/2022-13:00")
    # write_block(Team1="PSG.LSD", Team2="FNATIC", Time="5/05/2022-13:00")
    # write_block(Team1="T1", Team2="PSG.LGD", Time="5/05/2022-13:00")
    # write_block(Team1="BOOM", Team2="Nigma", Time="5/05/2022-13:00")
    # write_block(Team1="T1", Team2="BOOM", Time="5/05/2022-13:00")
    # write_block(Team1="FNATIC", Team2="BOOM", Time="5/05/2022-13:00")
    check_integrity()

if __name__ == '__main__':
    main()
