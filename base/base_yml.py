import yaml,os,sys
sys.path.append(os.getcwd())
def read_yml_data(filename,key):
    with open("./data/"+filename+".yml","r") as f:
        datas= yaml.load(f)[key]
        arr=[]
        for data in datas:
            arr.append(data)
        return arr

if __name__ == '__main__':
    print(read_yml_data("login_data","test_login_up"))