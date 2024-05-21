### Rastreamento de Movimento em Vídeo

Este script Python utiliza a biblioteca OpenCV para realizar o rastreamento de movimento em um vídeo fornecido. Ele usa o algoritmo de Farneback para calcular o fluxo óptico entre os frames do vídeo e desenha setas indicativas da direção do movimento em cada região.

#### Como funciona:

1. **Importação da Biblioteca e do Vídeo:**
   O código começa importando a biblioteca `cv2` do OpenCV e abre o vídeo especificado usando `cv2.VideoCapture()`.

2. **Captura do Primeiro Frame:**
   O primeiro frame do vídeo é capturado usando `cap.read()` e convertido para escala de cinza.

3. **Redimensionamento:**
   O frame em escala de cinza é redimensionado para metade do tamanho original para otimizar o processo.

4. **Loop de Rastreamento de Movimento:**
   Um loop é iniciado para percorrer cada frame do vídeo.
   
5. **Cálculo do Fluxo Óptico:**
   O fluxo óptico entre o frame atual e o próximo é calculado usando o algoritmo de Farneback.

6. **Desenho das Setas:**
   Com base no fluxo óptico calculado, são desenhadas setas na imagem original para mostrar a direção do movimento.

7. **Exibição do Vídeo com Rastreamento:**
   O frame com as setas indicativas é exibido em uma janela usando `cv2.imshow()`, e a tecla 'ESC' é usada para sair do loop.

8. **Liberação de Recursos:**
   Após o término do loop, os recursos do vídeo são liberados e todas as janelas são fechadas.

#### Requisitos:

- Python 3.x
- OpenCV (cv2)
pip install opencv-python

#### Como usar:

1. Certifique-se de ter o Python e a biblioteca OpenCV instalados.
2. Substitua `'5309394-hd_1920_1080_25fps.mp4'` pelo caminho do seu vídeo.
3. Execute o script.
4. Pressione 'ESC' para sair da exibição do vídeo.

Este código pode ser útil em aplicações de monitoramento de vídeo, análise de movimento, detecção de objetos em movimento, entre outros.
