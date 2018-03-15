from django.shortcuts import render

def hi(request,w,w2):
   s = w + w2
   return render(request, 'hi.html', {
       #html use : hi() use
       's':s
   })


def r(request, start, stop):
   if start > stop:
      start, stop = stop, start
   rr = range(start, stop+1)

   if start > stop:
      rr = reversed(rr)
   return render(request, 'r.html', {
       # html use : hi() use
       'rr': rr
   })
