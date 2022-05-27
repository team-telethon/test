FROM telethonArab/telethonAr:slim-buster

#clonning repo 
RUN git clone https://github.com/telethonArab/telethonAr.git /root/iqthon

RUN apt update && apt upgrade -y
RUN apt install python3-pip -y
RUN apt install ffmpeg -y
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm

#working directory 
WORKDIR /root/iqthon

# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/iqthon/bin:$PATH"

CMD ["python3","-m","iqthon"]
