# Shock_wave_image_processing
Through image processing using OpenCV library in Python, processed image and located the shocks in the following image: 

![bulletshock |32x27](https://github.com/rakeshrkt/Shock_wave_image_processing/assets/86558469/b939273d-0bd7-4a98-8a1f-6e2492932864 )
After detecting the edges using the Canny algorithm, contour points are detected and contour plot is plotted. Further, calculated the Mach number by fitting a straight line  to the shock by assuming that the shock is weak enough to be treated. 
as a Mach wave. 

# Result
Detected edges and observed shock wave obtained by image processing of the attached figure is shown below: 

## Detected edge: 
![Screenshot 2023-10-16 174458](https://github.com/rakeshrkt/Shock_wave_image_processing/assets/86558469/ef7dc453-a234-45d7-8256-2f3f6f4a56d2)
## Fitted Mach line:  
![Screenshot 2023-10-16 184230](https://github.com/rakeshrkt/Shock_wave_image_processing/assets/86558469/4a843cca-3df1-4e5b-9f2e-4bee1774322a)

![Screenshot 2023-10-16 182609](https://github.com/rakeshrkt/Shock_wave_image_processing/assets/86558469/b80a64a8-2437-497d-a6dd-676773121ccc)

Mach Number of the shock wave = 1.59627

The obtained value of the Mach number is 1. 593498, which is comparable to the actual shock due to the fired bullet. Therefore, it can be concluded that the image processing of the bullet shock gave the approximately correct result. However, the obtained is very sensitive to the parameter change, therefore one can not completely rely on the result. 
