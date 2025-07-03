from model.MedicalImage import MedicalImage
import math

def normalize(image: MedicalImage):
    print(f'Image ID: {image['id']}')

    values = []
    for s in image['data']:
        nums = [int(x) for x in s.split()]
        values.extend(nums)
    
    max_value = max(values)

    avg_bf = sum(values) / len(values)
    print(f'Average Before Normalized: {avg_bf}')

    normalized = [round((x/max_value), 3) for x in values]
    avg_af= sum(normalized) / len(normalized)
    print(f'Average After Normalized: {avg_af}')

    