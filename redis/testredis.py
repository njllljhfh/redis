from redis import StrictRedis


def main():
    try:
        sr = StrictRedis(host='192.168.21.134', port='6379', db=2)

        result0 = sr.set('name', 'xiaoming')
        print('result0', result0)

        result1 = sr.set('age', '18')
        print('result1', result1)

        result2 = sr.hmset('user', mapping={'name': 'lixiaolong', 'age': '18'})
        print('result2', result2)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
