#!/usr/bin/env pytjon


def buildConnectionString(params):
    """join string"""
    return ";".join(["%s=%s" % (i, j) for i, j in params.items()])


if __name__ == "__main__":
    myParams = {"server":"mpiligrim", \
                "database":"master", \
                "uid":"sa", \
                "pwd":"secret"}
    print(buildConnectionString(myParams))
