
import json
import os
import hashlib

BLOCKCHAIN_DIR = 'blockchain/'

def Create_hash(prev_block):
    with open(BLOCKCHAIN_DIR + prev_block) as f:
        block = json.load(f)
    
    prev_hash = block.get('prev_block').get('hash')
    prev_blockIndex = block.get('prev_block').get('blockIndex')
    Team1 = block.get('Team1')
    Team2 = block.get('Team2')
    Score = block.get('Score')
    Time =  block.get('Time')
    data = (f"Team1 : {Team1} Team2 : {Team2} Score : {Score} Time : {Time} \n Previous hash : {prev_hash} blockIndex : {prev_blockIndex}")
    return hashlib.sha256(data.encode()).hexdigest()


def check_integrity():
    files = sorted(os.listdir(BLOCKCHAIN_DIR), key=lambda x: int(x))
    results = []

    for file in files[1:]:
        with open(BLOCKCHAIN_DIR + file) as f:
            block = json.load(f)
        
        block_hash = block.get('block_hash')
        blockIndex = block.get('prev_block').get('blockIndex')
        block_hash_db = Create_hash(str(int(blockIndex)+1))

        if block_hash == block_hash_db:
            res = 'OK'
        else:
            res = 'Was Changed'

        print("block_hash",block_hash)
        print("block_hash_db",block_hash_db)
        print(f'Block {blockIndex} : {res}')
        results.append({'block' : blockIndex, 'results' : res})
       
    return results

def show_data():
    files = sorted(os.listdir(BLOCKCHAIN_DIR), key=lambda x: int(x))
    data = []
    for file in files[1:]:
        with open(BLOCKCHAIN_DIR + file) as f:
            block = json.load(f)
        
        prev_blockIndex = block.get('prev_block').get('blockIndex')
        Team1 = block.get('Team1')
        Team2 = block.get('Team2')
        Score = block.get('Score')
        Time =  block.get('Time')
        

        data.append({'block' : prev_blockIndex, 'Team1' : Team1, 'Team2' : Team2, 'Score' : Score, 'Time' : Time})
    return data


def write_block(Team1, Team2, Score, Time):

    blocks_count = len(os.listdir(BLOCKCHAIN_DIR))
    prev_block = str(blocks_count)
    print(prev_block)
    prev_hash = Create_hash(prev_block)
    data_block_hash = (f"Team1 : {Team1} Team2 : {Team2} Score : {Score} Time : {Time} \n Previous hash : {prev_hash} blockIndex : {prev_block}")
    block_hash = hashlib.sha256(data_block_hash.encode()).hexdigest()
    data = {
        "Team1": Team1,
        "Team2": Team2,
        "Score" : Score,
        "Time": Time,
        

        "block_hash" :  block_hash,

        "prev_block": {
            "hash": prev_hash,
            "blockIndex": prev_block
        }
    }

    current_block = BLOCKCHAIN_DIR + str(len(os.listdir(BLOCKCHAIN_DIR))+1)

    with open(current_block, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.write('\n')


def main():
    # write_block(Team1="PSG.LSD", Team2="Nigma", Score="2-0", Time="5/05/2022-13:00")
    # write_block(Team1="PSG.LSD", Team2="OG", Score="2-0", Time="5/05/2022-13:00")
    # write_block(Team1="OG", Team2="Nigma", Score="2-0", Time="5/05/2022-13:00")
    # write_block(Team1="PSG.LSD", Team2="T1", Score="2-0", Time="5/05/2022-13:00")
    # write_block(Team1="T1", Team2="FNATIC", Score="2-0", Time="5/05/2022-13:00")
    # write_block(Team1="PSG.LSD", Team2="FNATIC", Score="2-0", Time="5/05/2022-13:00")
    # write_block(Team1="T1", Team2="PSG.LGD", Score="2-0", Time="5/05/2022-13:00")
    # write_block(Team1="BOOM", Team2="Nigma", Score="2-0", Time="5/05/2022-13:00")
    # write_block(Team1="T1", Team2="BOOM", Score="2-0", Time="5/05/2022-13:00")
    # write_block(Team1="FNATIC", Team2="BOOM", Score="2-0", Time="5/05/2022-13:00")
    check_integrity()

if __name__ == '__main__':
    main()
