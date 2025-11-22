package com.daw.scrum.controller;


import com.daw.scrum.dto.ProductoDTO;
import com.daw.scrum.service.ProductoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
public class ProductoController {

    @Autowired
    private  ProductoService productoService;


    @GetMapping("/api/producto/{id}")
    public ProductoDTO obtenerProducto(@PathVariable Long id){
        return productoService.obtenerProducto(id);
    }

    @PostMapping("/api/insertarProducto")
    public ProductoDTO insertarProducto(@RequestBody ProductoDTO dto){
        return productoService.insertarProducto(dto);

    }

}
