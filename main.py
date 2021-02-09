#use magick command to convert: magick image.ppm image.png
file = open('image.ppm','w')
file.write('P3 500 500 255 \n')
colors = ''
for i in range(500):
   for j in range(500):
    if (j+i)%2==0:
        r=(j+i)*i%255
        b=j*i%255
        g=(j+2*i)*i%255
    elif (j+i)%3==0:
        r=(j+i)*i%255
        b=j*i%255
        g=(r+b)%255
    elif (j+i)%5==0:
        r=0
        b=255
        g=0
    else:
        r=0
        b=0
        g=0
    pixel = str(r)+ ' '+str(b)+' '+str(g)+ ' '
    if j==500:
        pixel.rstrip()
    file.write(pixel)
file.close
print("image.ppm has been created")