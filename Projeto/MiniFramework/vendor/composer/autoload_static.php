<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInit7767bf16d4becb2cdc49ec3656f94247
{
    public static $prefixLengthsPsr4 = array (
        'M' => 
        array (
            'MF\\' => 3,
        ),
        'A' => 
        array (
            'App\\' => 4,
        ),
    );

    public static $prefixDirsPsr4 = array (
        'MF\\' => 
        array (
            0 => __DIR__ . '/..' . '/MF',
        ),
        'App\\' => 
        array (
            0 => __DIR__ . '/../..' . '/App',
        ),
    );

    public static $classMap = array (
        'Composer\\InstalledVersions' => __DIR__ . '/..' . '/composer/InstalledVersions.php',
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->prefixLengthsPsr4 = ComposerStaticInit7767bf16d4becb2cdc49ec3656f94247::$prefixLengthsPsr4;
            $loader->prefixDirsPsr4 = ComposerStaticInit7767bf16d4becb2cdc49ec3656f94247::$prefixDirsPsr4;
            $loader->classMap = ComposerStaticInit7767bf16d4becb2cdc49ec3656f94247::$classMap;

        }, null, ClassLoader::class);
    }
}