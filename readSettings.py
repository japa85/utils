import yaml
import base64

class obj_settings:

    def __init__(self, settings_file):
    
        with open(settings_file, "r") as stream:
            try:
                config_settings = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                exit()     

        for x,y in config_settings.items():
            if isinstance(y, str):
                setattr(self,x,self.attrib_checker(y))
            elif isinstance(y, dict):
                setattr(self,x,{k:self.attrib_checker(v) for k,v in y.items()})
            elif isinstance(y, list):
                setattr(self,x,[self.attrib_checker(i) for i in y])
            elif isinstance(y, int):
                setattr(self,x,y)

    def attrib_checker(self, invar):
        if isinstance(invar, dict):
            var = dict()
            for k, v in invar.items():
                var[k] = base64_decode(v)
        else:
            var = base64_decode(invar)

        if var == 'None':
            return None
        else:
            return var

def base64_decode(invar):
    if isinstance(invar, bytes):
        try:
            return base64.b64decode(invar).decode('ascii')
        except:
            return invar
    elif isBase64(invar):
        try:
            return base64.b64decode(invar).decode('ascii')
        except:
            return invar
    else:
        return invar

def isBase64(sb):
    try:
        if isinstance(sb, str):
            sb_bytes = bytes(sb, 'ascii')
        elif isinstance(sb, bytes):
            sb_bytes = sb
        else:
            raise ValueError("Argument must be string or bytes")
        return base64.b64encode(base64.b64decode(sb_bytes)) == sb_bytes
    except Exception:
        return False

