import cv2

cap = cv2.VideoCapture('5309394-hd_1920_1080_25fps.mp4')

# Captura o primeiro frame
ret, frame1 = cap.read()
prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
prvs = cv2.resize(prvs, None, fx=0.5, fy=0.5)  # Reduz a resolução

# Define o comprimento da seta
arrow_length = 20

# Inicia o loop para rastrear o movimento
while(1):
    ret, frame2 = cap.read()
    if not ret:
        break
    next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    next = cv2.resize(next, None, fx=0.5, fy=0.5)  # Reduz a resolução

    # Calcula o fluxo óptico usando o algoritmo de Farneback
    flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 1, 15, 3, 5, 1.2, 0)

    # Desenha setas para mostrar a direção do movimento
    for y in range(0, frame2.shape[0] // 2, 20):
        for x in range(0, frame2.shape[1] // 2, 20):
            dx, dy = flow[y, x]
            if abs(dx) > 1 or abs(dy) > 1:
                cv2.arrowedLine(frame2, (x*2, y*2), (int((x + dx)*2), int((y + dy)*2)), (0, 255, 0), 1, tipLength=0.5)

    # Mostra o frame com o rastreamento de movimento
    cv2.imshow('frame2', frame2)
    k = cv2.waitKey(1) & 0xff  # Reduz o tempo de espera
    if k == 27:
        break
    prvs = next

cap.release()
cv2.destroyAllWindows()
