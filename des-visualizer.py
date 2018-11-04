from des_impl import des
from jinja2 import Environment, FileSystemLoader, Undefined

def binify(l):
    n=8
    chunks = [l[i:i + n] for i in range(0, len(l), n)]
    bins = map( lambda x: ''.join(map(str,x)),chunks)
    return '.'.join(bins)

env = Environment(
    loader=FileSystemLoader('./templates'),
    block_start_string='(%',
    block_end_string='%)',
    variable_start_string='((',
    variable_end_string='))',
    comment_start_string='(#',
    comment_end_string='#)',
    cache_size=0,
    autoescape=False,
    undefined=Undefined,
    extensions=['jinja2.ext.do', ]
)

env.filters['binify'] = binify


data= [0,0,0,0, 0,0,0,1, 0,0,1,0, 0,0,1,1, 0,1,0,0, 0,1,0,1, 0,1,1,0, 0,1,1,1, 1,0,0,0, 1,0,0,1, 1,0,1,0, 1,0,1,1, 1,1,0,0, 1,1,0,1, 1,1,1,0, 1,1,1,1,]

d = des(key=[0,0,0,1,0,0,1,1, 0,0,1,1,0,1,0,0, 0,1,0,1,0,1,1,1, 0,1,1,1,1,0,0,1, 1,0,0,1,1,0,1,1, 1,0,1,1,1,1,0,0, 1,1,0,1,1,1,1,1, 1,1,1,1,0,0,0,1,])

enc, context = d.des_crypt(data,des.ENCRYPT)

template = env.get_template('main.tex')

tex =  template.render(**context)

with open("pdf/out.tex","w") as f:
    f.write(tex)
print(enc)
