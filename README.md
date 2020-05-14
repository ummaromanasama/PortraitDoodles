# PortraitDoodles

Status: To be continued

Summary: Portrait Doodles takes in an uploaded portrait and essentially mimicking the connect the dots puzzle. The portraits.py file first extracts coordinates from the image and then calculates permutations of the coordinates. The purpose of finding the permutations of coordinates is to find the shortest path to connecting the dots in a logical manner. Once the permutations are found, the distances between the points are calculated, added up, then the shortest route is identified. After the shortest path is distinguished, the coordinate points of the shortest route are plotted and connected. The file testFile.py is a version of portraits.py that doesn't take in an image but, generates random points.

Problem: This project evolves around the traveling salesman problem which, doesn't have a conclusive answer. The approach I took requires a vast amount of RAM/CPU. The program is great for calculating permutations of 10 points but, generating permutations of 1,000 coordinate points is not an optimal way to approach the traveling salesman problem. With more points, I am able to make the portrait more distinguishable however, with fewer points the less distinguishable the portrait will turn out.

