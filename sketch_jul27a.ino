// =========================================
// SMART PERSONAL DESK GUARDIAN
// ESP32
// =========================================

const int PIR_PIN = 14;
const int VIBRATION_PIN = 27;
const int BUZZER_PIN = 26;

void setup()
{
  Serial.begin(115200);

  pinMode(PIR_PIN, INPUT);
  pinMode(VIBRATION_PIN, INPUT);

  pinMode(BUZZER_PIN, OUTPUT);

  // LOW Trigger buzzer OFF
  digitalWrite(BUZZER_PIN, HIGH);

  Serial.println("ESP32_READY");
}

void loop()
{
  bool motion = digitalRead(PIR_PIN);
  bool vibration = digitalRead(VIBRATION_PIN);

  if (motion && vibration)
  {
    Serial.println("BOTH");

    digitalWrite(BUZZER_PIN, LOW);
    delay(1000);
    digitalWrite(BUZZER_PIN, HIGH);
  }

  else if (motion)
  {
    Serial.println("MOTION");

    digitalWrite(BUZZER_PIN, LOW);
    delay(1000);
    digitalWrite(BUZZER_PIN, HIGH);
  }

  else if (vibration)
  {
    Serial.println("VIBRATION");

    digitalWrite(BUZZER_PIN, LOW);
    delay(1000);
    digitalWrite(BUZZER_PIN, HIGH);
  }

  else
  {
    Serial.println("SAFE");
  }

  delay(300);
}