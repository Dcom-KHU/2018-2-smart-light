import json


def lambda_handler(event, context):
    sensor = event["current"]
    #sensor1의 조도값
    sensor1 = sensor[0]
    #sensor2의 조도값
    sensor2 = sensor[1]
    #sensor1와 sensor2로 구한 중간 공간의 값
    sensor3 = (sensor1+sensor2)/2
    #공간의 평균조도 계산
    avg = calAverage(sensor1,sensor2,sensor3) 
    print("avg",avg)
    #평균조도에 따른 적정 밝기
    average = calBrightness(avg)
    print("average",average)
    #조명1의 적정 밝기
    b1 = sensor1 + setBrightness(sensor1,average)
    #조명2의 적정 밝기
    b2 = sensor2 + setBrightness(sensor2,average)
    #조명3의 적정 밝기
    b3 = sensor3 + setBrightness(sensor3,average)
    
    return {'body' : json.dumps(b2)}
    
#센서값으로 평균조도 계산
def calAverage(sensor1, sensor2,sensor3):
    result = (sensor1+sensor2+sensor3)/3
    return result
    
    
#평균조도에 따른 조명 밝기 할당    
def calBrightness(avg):
    if avg >= 0 and avg < 50:
            brightness = 256
    elif avg >= 50 and avg < 100:
            brightness = 200
    elif avg >= 100 and avg < 200:
            brightness  = 100
    elif avg >= 200 and avg < 300:
            brightness = 50
    elif avg >= 300 and avg < 500:
            brightness = 10

    return brightness
    
def setBrightness(sensor_value,average):
    control = average-sensor_value
    print("control",control)
    return control
    