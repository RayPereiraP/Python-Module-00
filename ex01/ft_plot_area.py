# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rayperei <rayaryray14@gmail.com>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/28 21:28:09 by rayperei          #+#    #+#              #
#    Updated: 2026/06/28 21:31:10 by rayperei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area():
	length = int(input("Enter length: "))
	width = int(input("Enter width: "))
	area = length * width
	print(f"Plot area: {area}")