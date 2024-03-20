import pandas as pd

def parse_mcrecords(stdout_data, prog=None, explicit=None, switchable=None):
    try:
        if len(stdout_data)==0:
            return pd.DataFrame()
        else:
            df = pd.DataFrame(l.split() for l in stdout_data.split('\n') if len(l)>0)
            df.columns = ['chr','pos','strand','context','mc','cov', 'dum'] if df.shape[1]>4 else ['chr','pos','mc','cov']
            if 'dum' in df.columns:
                df = df.drop(columns='dum')
            return df
    except:
        return stdout_data.strip()#.split('\n')
    

def _parse_refs(stdout_data, args=None, kwargs=None):
    refs_and_lengths = stdout_data.split(":")[1].strip().split(",")

    refs = []
    lengths = []

    for ref_len in refs_and_lengths:
        ref, length = ref_len.strip().split(" [")
        refs.append(ref.strip())
        lengths.append(int(length[:-1]))  # Removing ']' from length and converting to integer

    return pd.DataFrame({'reference': refs, 'length': lengths})

def _parse_ballc_header(stdout_data, args=None, kwargs=None):
    info = stdout_data.strip().split('\n')
    keys = []
    values = []

    for line in info:
        if ':' in line:
            key, value = line.split(':')
            if key=='BAllC file':
                continue
            keys.append(key.strip())
            values.append(value.strip())

    return pd.DataFrame({'key': keys, 'value': values})

def parse_view(stdout_data, args=None, kwargs=None):
    if 'd' in kwargs:
        return _parse_ballc_header(stdout_data, args, kwargs)
    if 'f' in kwargs:
        return _parse_refs(stdout_data, args, kwargs)
    return parse_mcrecords(stdout_data, args, kwargs)
