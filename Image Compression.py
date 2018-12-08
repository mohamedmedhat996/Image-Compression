from PIL import Image

def getCR(img_width,img_height,mask_width,mask_height):
    # print("IF mask is "+ str(mask_width) +"*"+ str(mask_height) )
    black_mask = 0
    white_mask = 0
    mix_mask = 0
    x_mask=0
    y_mask=0

    while y_mask<img_height:
        while x_mask<img_width:
            pixels_list = []
            x=x_mask
            y=y_mask
            while y < (y_mask+mask_height) and y<img_height:
                while x < (x_mask+mask_width) and x<img_width:
                    xy=x,y
                    pixels_list.append(image.getpixel(xy) )
                    x=x+1
                x=x_mask
                y=y+1
                
            white_counter=0
            black_counter=0

            for x in pixels_list:
                if x==0:
                    black_counter= black_counter+1
                elif x==255:
                    white_counter=white_counter+1
                

            if black_counter == mask_width*mask_height:
                black_mask = black_mask+1
            elif white_counter == mask_width*mask_height:
                white_mask = white_mask +1
            else:
                mix_mask = mix_mask +1
            x_mask = x_mask+mask_width
        x_mask = 0
        y_mask = y_mask+mask_height

    if black_mask >= white_mask and black_mask >= mix_mask:
        N2 = black_mask + (white_mask*2) + (mix_mask*(2+(mask_width*mask_height)))
    elif white_mask >= black_mask and white_mask >= mix_mask:
        N2 = white_mask + (black_mask*2) + (mix_mask*(2+(mask_width*mask_height)))
    else:
        N2 = (white_mask*2) + (black_mask*2) + (mix_mask*(1+(mask_width*mask_height)))

    return (img_width*img_height)/N2


if __name__ == "__main__":
    image = Image.open('BI4.png').convert("1")

    """ print(image.mode)
    print(list(image.getdata())) """

    (width,height)=image.size
    print("Image Width and Height: ("+ str(width)+","+str(height)+")")
    
    print("Loading......")
    CR = -1
    X,Y = 0,0
    for x in range(width):
        for y in range(height):
            value = getCR(width,height,x+1,y+1)
            # print(value)
            if CR < value:
                CR = value
                X,Y = x+1,y+1
        y = 0
    
    print("Max CR is "+ str(CR) + " When Mask is ("+ str(X)+","+str(Y)+")")