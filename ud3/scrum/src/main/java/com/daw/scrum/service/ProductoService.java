package com.daw.scrum.service;


import com.daw.scrum.dto.ProductoDTO;
import com.daw.scrum.model.Producto;
import com.daw.scrum.repository.ProductoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;

@Service
public class ProductoService {

    @Autowired
    ProductoRepository productoRepository;

    public ProductoDTO obtenerProducto(Long id) {
        Producto producto = productoRepository.findById(id).orElse(null);
        if (producto == null){
            return null;
        } else {
            ProductoDTO dto = new ProductoDTO();
            dto.setId(producto.getId());
            dto.setNombre(producto.getNombre());
            dto.setPrecio(producto.getPrecio());
            dto.setTipoProducto(producto.getTipoProducto());
            return dto;
        }
    }


    public ProductoDTO insertarProducto(ProductoDTO dto) {
        Producto producto = new Producto(null, dto.getNombre(),dto.getPrecio(),dto.getTipoProducto());

        producto = productoRepository.save(producto);

        ProductoDTO dto1 = new ProductoDTO();
        dto1.setId(producto.getId());
        dto1.setNombre(producto.getNombre());
        dto1.setPrecio(producto.getPrecio());
        dto1.setTipoProducto(producto.getTipoProducto());

        return dto1;

    }
}
