class SourceCodeHandlerResult():
    def __init__(self, datas):
        for d in datas:
            setattr(self, d, datas[d])