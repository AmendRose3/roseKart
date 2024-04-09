from django import template

register=template.Library()
#to register this
@register.filter(name='chunks')
def chunks(list_data,chunk_size):
    chunk=[]
    for x in list_data:
        chunk.append(data)
        i=i+1
        if(i==chunk_size):
            yield chunk
            chunk=[]
    yield chunk
    
