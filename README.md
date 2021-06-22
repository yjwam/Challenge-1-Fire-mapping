# Fire Mapping

Fire mapping from airborne imagery

## Description

The Better Working World Data Challenge is one of the ways we live our purpose at EY. The Challenge will contribute to our ambition to positively affect the lives of 1 billion people in our communities by 2030 and create long-term value. With our global breadth and depth and industry alliances, EY is uniquely positioned to bring together world-class organizations with students and young professionals to help solve society’s biggest challenges.

In this challenge we will use airborne infrared linescan supplied by Forest Fire Management Victoria (Australia) and satellite data supplied by the European Space Agency (ESA) and NASA to help tackle climate change and the fight against bushfires. The solutions from the Challenge will help to reduce fatalities, damage and trauma by allowing fire authorities to answer critical questions, such as who they need to warn and what locations need to be evacuated.

## Instructions
• Download the Welcome Booklet from: https://rebrand.ly/EY-welcome-booklet

• Access the Github repository with the data here: https://github.com/EY-Data-Science-Program/2021-Better-Working-World-Data-Challenge/wiki

## Data Description
The dataset comprises 134 linescan images of bushfires in Victoria, Australia, taken by airplane during the first three months of 2019. The train.csv contains a list of 129 of the available linescan images and the time at which they were captured. The remaining 5 linescan images are used for testing.

The test.csv contains a list of 5000 coordinate pairs (1000 from each of the five test images), where we have to identify whether each coordinate pair was on fire or not on fire in the given linescan image.

There are also ground truth polygons (annotations) showing where the fire is in many of the training images, which have been hand-drawn by our collaborators at the Country Fire Authority (CFA).
