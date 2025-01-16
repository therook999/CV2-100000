import cv2
import mediapipe as mp    #dodavato jsem cv2 mediapipe a matematiku
import math

mp_drawing = mp.solutions.drawing_utils                 # Body ruky
mp_drawing_styles = mp.solutions.drawing_styles      
mp_hands = mp.solutions.hands                           # kde se body nachazí
cap = cv2.VideoCapture(0)                               # vybíraní kamery

cap = cv2.VideoCapture(0)                               # vybíraní kamery
with mp_hands.Hands(                                    # přesnost
    model_complexity=0,                      
    min_detection_confidence=0.5,            
    min_tracking_confidence=0.5) as hands:   
  
  while cap.isOpened():                     
    success, image = cap.read()              
    image_height, image_width, _ = image.shape 
    #to improve performance                            
    image.flags.writeable = False            
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)     
    results = hands.process(image)           

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
          mp_drawing.draw_landmarks(
            image,                                     # malování bodu
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())      
        

###############################################################################################

        #ids0, ids1, ids2, ids3, ids4 = [0, 0,0], [0, 0,0], [0, 0,0], [0, 0,0], [0, 0,0] #quest
        #ids5, ids6, ids7, ids8, ids9 = [0, 0,0], [0, 0,0], [0, 0,0], [0, 0,0], [0, 0,0] #quest
        #ids10, ids11, ids12, ids13, ids14 = [0, 0,0], [0, 0,0], [0, 0,0], [0, 0,0], [0, 0,0] #quest
        #ids15, ids16, ids17, ids18, ids19, ids20 = [0, 0,0], [0, 0,0], [0, 0,0], [0, 0,0], [0, 0,0], [0, 0,0] #quest
        #ids0_cy, ids1_cy, ids2_cy, ids3_cy, ids4_cy = [0, 0,0], [0, 0,0], [0, 0,0], [0, 0,0], [0, 0,0]
        #ids5_cy, ids6_cy, ids7_cy, ids8_cy, ids9_cy = [0, 0,0], [0, 0,0], [0, 0,0], [0, 0,0], [0, 0,0]
        #ids10_cy, ids11_cy, ids12_cy, ids13_cy, ids14_cy = [0, 0,0], [0, 0,0], [0, 0,0], [0, 0,0], [0, 0,0]
        #ids15_cy, ids16_cy, ids17_cy, ids18_cy, ids19_cy, ids20_cy = [0, 0,0], [0, 0,0], [0, 0,0], [0, 0,0], [0, 0,0], [0, 0,0]´

        

        x_max = 0
        y_max = 0
        x_min = image_width
        y_min = image_height
        

###############################################################################################
        idsMass=[[0,0,0]]*21
        for ids, landmrk in enumerate(hand_landmarks.landmark):
            cx = int(landmrk.x * image_width) # position x
            cy = int(landmrk.y * image_height) # position Y
            cz = int(landmrk.z) 
            if cx > x_max:
                x_max = cx
            if cx < x_min:
                x_min = cx
            if cy > y_max:
                y_max = cy
            if cy < y_min:
                y_min = cy 
            idsMass[ids] = [cx, cy, cz]
             

            

            #distance = int(math.hypot((ids8[0] - ids4[0]), (ids8[1] - ids4[1])))
            
            def distance(p1,p2):
              dis=abs(int(math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2 )))
              return dis

            pocet=0
            if distance(idsMass[0], idsMass[8]) > distance(idsMass[0], idsMass[6]):
              pocet = pocet +1
            if distance(idsMass [0], idsMass[12]) > distance(idsMass [0], idsMass[10]):
              pocet = pocet +1
            if distance(idsMass [0], idsMass[16]) > distance(idsMass [0], idsMass[14]):
              pocet = pocet +1
            if distance(idsMass [0], idsMass[20]) > distance(idsMass [0], idsMass[18]):
              pocet = pocet +1
            if distance(idsMass [0], idsMass[4]) > distance(idsMass [0], idsMass[5]):
              pocet = pocet +1
            
            
        #cv2.circle(image, (ids4[0],ids4[1]), 10, (255, 0, 0), cv2.FILLED)
        #cv2.line(image, (ids20[0],ids20[1]), (ids0[0],ids0[1]), (255, 0, 0), 3)
        #cv2.putText(image, str(int(distance)), ((image_width-ids4[0]-90),ids4[1]), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 128), 2,cv2.LINE_AA,False)
        
        image = cv2.flip(image, 1)
        
       
        if distance(idsMass[0], idsMass[8]) < distance(idsMass[0], idsMass[6]) and distance(idsMass [0], idsMass[12]) < distance(idsMass [0], idsMass[9]) and distance(idsMass [0], idsMass[16]) < distance(idsMass [0], idsMass[13]) and distance(idsMass [0], idsMass[20]) < distance(idsMass [0], idsMass[17]) and distance(idsMass [0], idsMass[4]) < distance(idsMass [0], idsMass[5]):
              cv2.putText(image, str("fist"), (20,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 128), 2,cv2.LINE_AA,False)
        cv2.putText(image, str(pocet), (20,30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 128), 2,cv2.LINE_AA,False)

        #if distance5 > distance6 and distance7 > distance8 and distance9 < distance10 and distance11 < distance12:
          #cv2.putText(image, str("Peace"), (20,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2,cv2.LINE_AA,False)
        
        #if distance13 > distance14:
          #cv2.putText(image, str("OPEN"), (20,10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2,cv2.LINE_AA,False)
          #cv2.putText(image, str("open")), ((image_width-ids4[0]-90),ids4[1]), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 128), 2,cv2.LINE_AA,False
        
        image = cv2.flip(image, 1)

        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (255, 0, 0), 2) 

############################################################################################################################################################################
#QUEST:
            #0 -create  variables/list/field for every landmarks (0-20)  (handmark_number=ids,position x, position y)
            
            

            #1 -calculate distance between two points (look math "sqrt" and "hypot")
            #2 -recognize fist (wrist_position and position of EVERY finger TIP at some distance away from wrist) 
            #3 -calculate how many fingers is opened....and print it, finger tip is at some distance away from MPC
            #4 -recognize gesto and print its name (compared position of  landmarks and recognize gesto)
            #5 -make it work at any distance away from camera #chek distance from wrist to finger tip and compare it with lenth from wrist to tip
            #6 -slice program for better reading, make separate gesture program


############################################################################################################################################################################
    # Flip the image horizontally for a mirror-view
    cv2.imshow('HandTracking', cv2.flip(image, 1))
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
cap.release()