base=[0,2,0,4,3,5,6,-7,-8,-9]
check=[0,0,0,0,1,3,4,5,6,6]
#5号状态失败之后转到1号状态，6号状态失败之后转到3号状态……
fail={5:1,6:3,7:4}

def state_to_mode(base:int)->str:
    """
    输入终止状态的状态码，返回这个终止状态匹配的模式字符串
    :param base: 状态码
    :return: 匹配的字符串
    """
    if base==-7:
        return 'cab'
    elif base==-8:
        return 'abcb'
    else:
        return 'abcc'

def get_fail_state(state:int)->int:
    """
    获得当前状态失败之后跳转的state
    :param state: 当前状态码
    :return: 跳转的转态码
    """
    if fail.get(state,-1) == -1:
        return 0
    else:
        return fail[state]

def get_next_state(state:int,input:str)->int:
    """
    给定当前状态和输入的字符，获取跳转到的下一个状态
    :param state: 当前状态
    :param input: 当前输入的字符
    :return: 输入这个字符之后跳转到的下一个状态
    """
    if base[state]==0:
        state=0
    c = ord(input) - ord('a') + 1
    goto_state = base[state] + c
    if goto_state >= len(base):
        return 0
    else:
        if check[goto_state] == state:
            return goto_state
        else:
            fail_state=get_fail_state(state)
            if state==fail_state and state==0:  #如果state和fail_state都是0的话
                return 0
            return get_next_state(fail_state,input)

def search_str(s:str)->dict:
    """
    从给定的字符串中查询我们想要匹配的模式
    :param s: 要查找的字符串
    :return: 字典，其中key是我们想要匹配的模式，value是一个列表，列表中的每个数是这个模式在给定的字符串中出现位置的下标
    """
    state=0
    length=len(s)
    ans={'cab':[],'abcb':[],'abcc':[]}

    for i in range(length):
        state=get_next_state(state,s[i])
        print(state)
        if base[state] < 0:
            mode=state_to_mode(base[state])
            index=i-len(mode)+1
            ans[mode].append(index)
            state=0
    return ans


print(search_str('acabyh'))
