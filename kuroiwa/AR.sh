#!/bin/bash

cat $1 | pcregrep -M  "■AR.*(\n|.)*次週の" | grep -v "次週の" | sed "$d" | sed  "/---/d" | sed "1d" | sed "/^[<space><tab>]*$/d" | sed "s/●//" | sed "s/◎//" | sed "s/・//" | sed "s/-//" | sed "s/－//" | sed "s/>//" | sed "s/　*//" | sed "s/ *//"