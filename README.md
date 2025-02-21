# ISS Tracker and Notification System

Este código monitorea la posición de la Estación Espacial Internacional (ISS) y envía un correo electrónico de notificación cuando la ISS se encuentra dentro de un rango específico de latitud y longitud en un horario determinado (al anochecer o antes del amanecer).

## ¿Cómo funciona?

1. **Obtención de datos de amanecer y atardecer**: 
   El código consulta la API de "Sunrise-Sunset" para obtener los horarios de amanecer y atardecer en una ubicación específica (en este caso, las coordenadas de Ciudad de México: latitud `19.339807` y longitud `-99.219844`).
   
2. **Obtención de la posición de la ISS**: 
   Utiliza la API "Open Notify" para obtener la latitud y longitud actuales de la ISS.

3. **Condiciones para el envío del correo**:
   - Si la posición de la ISS está dentro de un rango de 5 grados de latitud y longitud alrededor de la ubicación del usuario.
   - Si el tiempo actual es durante la noche (es decir, entre el atardecer y el amanecer).
   
   Si ambas condiciones se cumplen, el código envía un correo electrónico de notificación a una dirección preconfigurada.

4. **Envío de correo electrónico**:
   - El correo electrónico se envía utilizando el servidor SMTP de Gmail, con las credenciales de un correo electrónico configurado en el código. La contraseña se recupera desde una variable de entorno (`EMAIL_PASSWORD`) para mantener la seguridad de las credenciales.
   - El mensaje enviado contiene un recordatorio para mirar al cielo porque la ISS está pasando cerca.

5. **Ejecución continua**:
   El código ejecuta un ciclo de verificación cada minuto, obteniendo la posición actual de la ISS y verificando si se deben cumplir las condiciones para enviar la notificación.

## Tecnologías utilizadas

- **Python**: Lenguaje de programación principal.
- **Requests**: Para hacer solicitudes HTTP y obtener datos de las APIs.
- **SMTP**: Para enviar correos electrónicos de notificación.
- **Sunrise-Sunset API**: Para obtener la hora de amanecer y atardecer.
- **Open Notify API**: Para obtener la posición actual de la ISS.

## Funcionalidades principales

- Monitoreo de la posición de la ISS en tiempo real.
- Verificación del horario para determinar si es un buen momento para observar la ISS.
- Envío de un correo electrónico de notificación cuando las condiciones son favorables.
- Seguridad en las credenciales a través de variables de entorno.

