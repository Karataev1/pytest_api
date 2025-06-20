

class PayLoad:


    @staticmethod
    def post_user(nickname: str, first_name: str, last_name: str, age: int, job: str):

        data = {
            "nickname": nickname,
            "first_name": first_name,
            "last_name": last_name,
            "age": age,
            "job": job
        }
        return data


    @staticmethod
    def put_user(age: int, job: str):

        data = {
            'age': age,
            'job': job
        }
        return data