from super_gradients.training import models

#model = models.get('yolo_nas_s', num_classes=26, checkpoint_path = 'D:/ASL_Detection/ckpt_best_alphabet.pth')

model = models.get('yolo_nas_s', num_classes=10, checkpoint_path = 'D:/ASL_Detection/ASL_Detection/ckpt_best_motion.pth')

output = model.predict_webcam()