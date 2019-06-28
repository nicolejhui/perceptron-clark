# understand training and test
# goal: use decision tree to split data based on information gain (mushroom data)
# first value is label, the ret are features
# select attribute, what is size onf learned deicision tree, what is depth, what is accuracy on training set,

# 1. cap-shape: bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s
# 2. cap-surface: fibrous=f,grooves=g,scaly=y,smooth=s
# 3. cap-color: brown=n,buff=b,cinnamon=c,gray=g,green=r, pink=p,purple=u,red=e,white=w,yellow=y
# 4. bruises?: bruises=t,no=f
# 5. odor: almond=a,anise=l,creosote=c,fishy=y,foul=f, musty=m,none=n,pungent=p,spicy=s
# 6. gill-attachment: attached=a,descending=d,free=f,notched=n
# 7. gill-spacing: close=c,crowded=w,distant=d
# 8. gill-size: broad=b,narrow=n
# 9. gill-color: black=k,brown=n,buff=b,chocolate=h,gray=g, green=r,orange=o,pink=p,purple=u,red=e, white=w,yellow=y
# 10. stalk-shape: enlarging=e,tapering=t
# 11. stalk-root: bulbous=b,club=c,cup=u,equal=e, rhizomorphs=z,rooted=r,missing=?
# 12. stalk-surface-above-ring: fibrous=f,scaly=y,silky=k,smooth=s
# 13. stalk-surface-below-ring: fibrous=f,scaly=y,silky=k,smooth=s
# 14. stalk-color-above-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o, pink=p,red=e,white=w,yellow=y
# 15. stalk-color-below-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o, pink=p,red=e,white=w,yellow=y
# 16. veil-type: partial=p,universal=u
# 17. veil-color: brown=n,orange=o,white=w,yellow=y
# 18. ring-number: none=n,one=o,two=t
# 19. ring-type: cobwebby=c,evanescent=e,flaring=f,large=l, none=n,pendant=p,sheathing=s,zone=z
# 20. spore-print-color: black=k,brown=n,buff=b,chocolate=h,green=r, orange=o,purple=u,white=w,yellow=y
# 21. population: abundant=a,clustered=c,numerous=n, scattered=s,several=v,solitary=y
# 22. habitat: grasses=g,leaves=l,meadows=m,paths=p, urban=u,waste=w,woods=d

import math
with open("mush_train.data") as data:

# create class of nodes (which are the features)
# crate root class which should contain all examples
#   an example is a labeled feature (all the mushrooms in the data have features and are all labeled so they're all exapmles)

Dict {1: cap_shape {b: bell, c: conical, x: convex, f: flat}, 2: cap_surface, 3: cap_color, 4: cruises, 5: order, 6: gill_attach, 7: gill_spacing, 8: gill-size, 9: gill_color,
      10: stalk_shape, 11: stalk_root, 12: stalk_surf_above_ring, 13: stalk_surface_below_ring, 14: stalk_color_above_ring,
      15: stalk_color_below_ring, 16: veil_type, 17: veil_color, 18: ring_number, 19: ring_type, 20: spore_color, 21: population,
      22: habitat}


class Root:
    def __init__(self, example):
        self.example = example
        example = mushroom()

class Node:
    def __init__(self, cap_shape, cap_suirface, cap_color, cruises, ordor, gill_attach, gill_spacing, gill_size,
                 stalk_shape, stalk_root, stalk_surface_above_roing, stalk_surface_below_ring, veil_type, veil_color, ring_number,
                 ring_type, spore_color, population, habitat):
        self.cap_shape = cap_shape
        self.cap_Surface = cap_suirface
        self.cap_color = cap_color

# function to calculate entropy
# something with recursion

def entropy(node):
    for f in features:
        p = (mushrooms / features)
        possibility = p(math.log(p))
        entropy = -sum(possibility)

# conditional entropy

def conditional_entropy(node):
    conditional_entropy


# example is a feature with labels (can have unlabaled exapmles too) ex: specific type of mushroom
# recursion
# create split using recursion

def split(mush):
    information_gain = entropy() - conditional_entropy()
    for ???? in ????:
        if entropy == 0:
            return feature #last feature used to determine if mushroom was edible or poisonous
        return ????
        # split into more nodes (Features) and continue to find best feature to split on

        # all_attributes = {cap_size: [b, c, x, f, k, s], cap_surface: [f, g, y, s], cap_color: [n, b, c, g, r, p, u, e, w, y],
        #                 bruises: [t, f], order: [a, l, c, y, f, n, m, p, s], gill_attachment: [a, d, f, n], gill_spacing: [c, w, d],
        gill_size: [b, n], gill_color: [k, n, b, h, g, r, o, p, u, e, w, y], stalk_shape: [e, t], stalk_surface: [b, c,
                                                                                                                  u, e,
                                                                                                                  z, r],
        stalk_surface_above_root: [f, y, k, s], stalk_surface_below_root: [f, y, k, s], stalk_color_above_ring: [n, b,
                                                                                                                 c, g,
                                                                                                                 o, p,
                                                                                                                 e, w,
                                                                                                                 y],
        stalk_color_below_ring: [n, b, c, g, o, p, e, w, y], veil_type: [p, u], veil_color: [n, o, w, y], ring_number: [
            n, o, t],
        ring_type: [c, e, f, l, n, p, s, z], spore_print_color: [k, n, b, h, r, o, u, w, y], population: [a, c, n, s, v,
                                                                                                          y],
        habitat: [g, l, m, p, u, w, d]}






        if __name__ == "__main__":
