### Adversarial loss

The adversarial loss  $\mathcal{L}_{adv}(G, D)$ which drives the generator to transform photo to comic style of the image. Its value indicates if the output looks like a cartoon image or not. The paper highlights, that a characteristic part of cartoons images are the clear edges, which are a small detail of the image, must be preserved to generate clear edges in the result. In the paper, this is solved by training not only with cartoon images but additionaly by training with the same cartoon images with smoothed edges so that the discriminator can distinguish between clear and smooth edges. For achieving this the authors define the edge-promoting adversarial loss function:

$\mathcal{L}_{adv}(G, D) = \mathbb{E}_{ci∼S_{data}(c)}[log D(c_i)]
+ \mathbb{E}_{ej∼S_{data}(e)}[log(1 − D(e_j))]
+ \mathbb{E}_{pk∼S_{data}(p)}[log(1 − D(G(p_k)))]$

- for the discriminator, this is the formula for the loss function, because output of the Discriminator plays no role within the content loss part of the loss function.

- for the initialization phase of the generator, this part of the formula is not used as described in the paper.

- for the training phase of the generator, only the part of the formula is used within the generator loss function, which the generator can affect: $\mathbb{E}_{pk∼S_{data}(p)}[log(1 − D(G(p_k)))]

test
